#!/usr/bin/python3

import imp
import os
import shutil
import json

# Import script
pathlinker = imp.load_source('pathlinker', 'pathlinker')

def test_result_everything_possible_linked(original_dir_test, destination_dir_test, tracked_paths):

    for tracked_path in tracked_paths:

        tracked_path_home = os.path.join(original_dir_test, tracked_path)
        tracked_path_backup = os.path.join(destination_dir_test, tracked_path)

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

def test_result_nothing_gets_changed(original_dir_test, destination_dir_test, tracked_paths):

    for tracked_path in tracked_paths:

        tracked_path_home = os.path.join(original_dir_test, tracked_path)
        tracked_path_backup = os.path.join(destination_dir_test, tracked_path)

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

def test_pathlinker(test_name, run_script_lambda, test_result_function):

    print(f'### {test_name}')

    # Directories for testing
    CURR_DIR = os.path.expandvars('$PWD')
    TEST_DIR = os.path.join(CURR_DIR, 'pathlinker_test_dir')

    ORIGINAL_DIR = os.path.join(TEST_DIR, 'original_dir')
    ORIGINAL_DIR_TEST = os.path.join(TEST_DIR, 'original_dir_test')
    DESTINATION_DIR = os.path.join(TEST_DIR, 'destination_dir')
    DESTINATION_DIR_TEST = os.path.join(TEST_DIR, 'destination_dir_test')

    # Test files
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
    SETTINGS_FILE_TEST = os.path.join(TEST_DIR, 'pathlinker_test.json')

    # Setup testing environment
    
    # Make test copies
    shutil.copytree(ORIGINAL_DIR, ORIGINAL_DIR_TEST, symlinks=True)
    shutil.copytree(DESTINATION_DIR, DESTINATION_DIR_TEST, symlinks=True)
    shutil.copyfile(SETTINGS_FILE, SETTINGS_FILE_TEST)

    # Add test symlink
    os.symlink(os.path.join(DESTINATION_DIR_TEST, 'TEST_SYM_RIGHT_YES'), os.path.join(ORIGINAL_DIR_TEST, 'TEST_SYM_RIGHT_YES'))

    # Setup pathlink.json settings
    with open(SETTINGS_FILE_TEST, 'r') as fp:
        settings_content = json.load(fp)
    settings_content['original_dir'] = ORIGINAL_DIR_TEST
    settings_content['destination_dir'] = DESTINATION_DIR_TEST
    with open(SETTINGS_FILE_TEST, 'w') as fp:
        json.dump(settings_content, fp, indent=4, sort_keys=True)

    try:
        run_script_lambda(SETTINGS_FILE_TEST)
    except AssertionError as error:
        print(f'pathlinker script error: {error}')

    test_result_function(ORIGINAL_DIR_TEST, DESTINATION_DIR_TEST, TRACKED_PATHS)

    # Clean testing dirs
    shutil.rmtree(ORIGINAL_DIR_TEST)
    shutil.rmtree(DESTINATION_DIR_TEST)
    os.remove(SETTINGS_FILE_TEST)

test_pathlinker('TEST 1 (execute_linking=True)', 
    lambda settings_file: pathlinker.pathlink(settings_file, execute_linking=True, automatic_yes=True),
    test_result_everything_possible_linked)

test_pathlinker('TEST 2 (execute_linking=False)', 
    lambda settings_file: pathlinker.pathlink(settings_file, execute_linking=False),
    test_result_nothing_gets_changed)