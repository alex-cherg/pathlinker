#!/usr/bin/python3

import imp
# from pathlinker import pathlink
import os
import shutil

pathlinker = imp.load_source('pathlinker', 'pathlinker')

CURR_DIR = os.path.expandvars('$PWD')
TEST_DIR = os.path.join(CURR_DIR, 'pathlinker_test_dir')

ORIGINAL_DIR = os.path.join(TEST_DIR, 'original_dir')
ORIGINAL_DIR_TEST = os.path.join(TEST_DIR, 'original_dir_test')
DESTINATION_DIR = os.path.join(TEST_DIR, 'destination_dir')
DESTINATION_DIR_TEST = os.path.join(TEST_DIR, 'destination_dir_test')

# Setup test link
# TODO: Find how to force this to execute
# os.symlink(source=os.path.join(DESTINATION_DIR_TEST, 'TEST_SYM_RIGHT_YES'), link_name=os.path.join(ORIGINAL_DIR, 'TEST_SYM_RIGHT_YES'))

TRACKED_PATHS = [
    'TEST_NO_YES',
    'TEST_SYM_RIGHT_YES',
    'TEST_SYM_WRONG_YES',
    'TEST_DIR_YES',
    'TEST_FILE_YES',
    'TEST_NO_NO',
    'TEST_SYM_NO',
    'TEST_DIR_NO',
    'TEST_FILE_NO'
]

SETTINGS_FILE = os.path.join(TEST_DIR, 'pathlinker.json')

def test_everything_possible_linked(original_dir_test, destination_dir_test, tracked_path):

    tracked_path_home = os.path.join(ORIGINAL_DIR_TEST, tracked_path)
    tracked_path_backup = os.path.join(DESTINATION_DIR_TEST, tracked_path)

    try:
        if (tracked_path == 'TEST_NO_YES' 
                or tracked_path == 'TEST_SYM_RIGHT_YES'
                or tracked_path == 'TEST_SYM_WRONG_YES'
                or tracked_path == 'TEST_DIR_YES'
                or tracked_path == 'TEST_FILE_YES'
                or tracked_path == 'TEST_DIR_NO'
                or tracked_path == 'TEST_FILE_NO'):
            assert (os.path.islink(tracked_path_home))
            assert (os.readlink(tracked_path_home) == tracked_path_backup)
            assert (os.path.exists(tracked_path_backup))
        elif tracked_path == 'TEST_NO_NO':
            assert (not os.path.exists(tracked_path_home))
            assert (not os.path.islink(tracked_path_home))
            assert (not os.path.exists(tracked_path_backup))
            assert (not os.path.islink(tracked_path_backup))
        elif tracked_path == 'TEST_SYM_NO':
            assert (os.path.islink(tracked_path_home))
            assert (not os.path.exists(tracked_path_backup))
            assert (not os.path.islink(tracked_path_backup))
        else:
            raise Exception('Unknown test tracked path!')
        
        print(f'Test passed: {tracked_path}')

    except AssertionError as error:
        print(f'Test failed: {tracked_path}')
        print(error)

def test_nothing_gets_changed(original_dir_test, destination_dir_test, tracked_path):

    tracked_path_home = os.path.join(ORIGINAL_DIR_TEST, tracked_path)
    tracked_path_backup = os.path.join(DESTINATION_DIR_TEST, tracked_path)

    try:
        if tracked_path == 'TEST_NO_YES':
            assert (not os.path.exists(tracked_path_home))
            assert (os.path.exists(tracked_path_backup))
        elif tracked_path == 'TEST_SYM_RIGHT_YES':
            assert (os.path.islink(tracked_path_home))
            assert (os.readlink(tracked_path_home) == tracked_path_backup)
            assert (os.path.exists(tracked_path_backup))
        elif tracked_path == 'TEST_SYM_WRONG_YES':
            assert (os.path.islink(tracked_path_home))
            assert (not os.readlink(tracked_path_home) == tracked_path_backup)
            assert (os.path.exists(tracked_path_backup))
        elif tracked_path == 'TEST_DIR_YES':
            assert (os.path.isdir(tracked_path_home))
            assert (os.path.exists(tracked_path_backup))
        elif tracked_path == 'TEST_FILE_YES':
            assert (os.path.isfile(tracked_path_home))
            assert (os.path.exists(tracked_path_backup))
        elif tracked_path == 'TEST_NO_NO':
            assert (not os.path.exists(tracked_path_home))
            assert (not os.path.islink(tracked_path_home))
            assert (not os.path.exists(tracked_path_backup))
            assert (not os.path.islink(tracked_path_backup))
        elif tracked_path == 'TEST_SYM_NO':
            assert (os.path.islink(tracked_path_home))
            assert (not os.path.exists(tracked_path_backup))
            assert (not os.path.islink(tracked_path_backup))
        elif tracked_path == 'TEST_DIR_NO':
            assert (os.path.isdir(tracked_path_home))
            assert (not os.path.exists(tracked_path_backup))
            assert (not os.path.islink(tracked_path_backup))
        elif tracked_path == 'TEST_FILE_NO':
            assert (os.path.isfile(tracked_path_home))
            assert (not os.path.exists(tracked_path_backup))
            assert (not os.path.islink(tracked_path_backup))
        else:
            raise Exception('Unknown test tracked path!')
        
        print(f'Test passed: {tracked_path}')

    except AssertionError as error:
        print(f'Test failed: {tracked_path}')
        print(error)

# TEST 1 (prompt_answer = True)

print("### TEST 1 (prompt_annswer = True)")

shutil.copytree(ORIGINAL_DIR, ORIGINAL_DIR_TEST, symlinks=True)
shutil.copytree(DESTINATION_DIR, DESTINATION_DIR_TEST, symlinks=True)

try:
    pathlinker.pathlink(SETTINGS_FILE, execute_linking=True, automatic_yes=True)
except AssertionError as error:
    print("synchronise_configs script encountered error")

for tracked_path in TRACKED_PATHS:

    test_everything_possible_linked(ORIGINAL_DIR_TEST, DESTINATION_DIR_TEST, tracked_path)

shutil.rmtree(ORIGINAL_DIR_TEST)
shutil.rmtree(DESTINATION_DIR_TEST)

# TEST 2 (prompt_answer = False)

print("### TEST 2 (prompt_annswer = False)")

shutil.copytree(ORIGINAL_DIR, ORIGINAL_DIR_TEST, symlinks=True)
shutil.copytree(DESTINATION_DIR, DESTINATION_DIR_TEST, symlinks=True)

try:
    pathlinker.pathlink(SETTINGS_FILE, execute_linking=False)
except AssertionError as error:
    print("synchronise_configs script encountered error")

for tracked_path in TRACKED_PATHS:
    test_nothing_gets_changed(ORIGINAL_DIR_TEST, DESTINATION_DIR_TEST, tracked_path)

shutil.rmtree(ORIGINAL_DIR_TEST)
shutil.rmtree(DESTINATION_DIR_TEST)

# End of tests

# TODO: See before
# Remove test link
# os.unlink(os.path.join(ORIGINAL_DIR, 'TEST_SYM_RIGHT_YES'))






