#!/usr/bin/python3

import imp
import os
import shutil
import json

# Import script
pathlinker = imp.load_source('pathlinker', 'pathlinker')

def test_result_everything_possible_linked(original_dir_test, destination_dir_test, tracked_paths):

    print('*** test_result_everything_possible_linked ***')

    for tracked_path in tracked_paths:

        tracked_path_home = os.path.join(original_dir_test, tracked_path)
        tracked_path_backup = os.path.join(destination_dir_test, tracked_path)

        try:
            if (tracked_path == 'TEST_NO_FILE' 
                    or tracked_path == 'TEST_SYM_RIGHT_FILE'
                    or tracked_path == 'TEST_SYM_RIGHT_DIR'
                    or tracked_path == 'TEST_SYM_WRONG_FILE'
                    or tracked_path == 'TEST_DIR_FILE'
                    or tracked_path == 'TEST_FILE_FILE'
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

        except AssertionError as error:
            print(f'FAILED TEST: {tracked_path}')
            print(error)

def test_result_nothing_gets_changed(original_dir_test, destination_dir_test, tracked_paths):

    print('*** test_result_nothing_gets_changed ***')

    for tracked_path in tracked_paths:

        tracked_path_home = os.path.join(original_dir_test, tracked_path)
        tracked_path_backup = os.path.join(destination_dir_test, tracked_path)

        try:
            if tracked_path == 'TEST_NO_FILE':
                assert (not os.path.exists(tracked_path_home))
                assert (os.path.exists(tracked_path_backup))
            elif (tracked_path == 'TEST_SYM_RIGHT_FILE'
                    or tracked_path == 'TEST_SYM_RIGHT_DIR'):
                assert (os.path.islink(tracked_path_home))
                assert (os.readlink(tracked_path_home) == tracked_path_backup)
                assert (os.path.exists(tracked_path_backup))
            elif tracked_path == 'TEST_SYM_WRONG_FILE':
                assert (os.path.islink(tracked_path_home))
                assert (not os.readlink(tracked_path_home) == tracked_path_backup)
                assert (os.path.exists(tracked_path_backup))
            elif tracked_path == 'TEST_DIR_FILE':
                assert (os.path.isdir(tracked_path_home))
                assert (os.path.exists(tracked_path_backup))
            elif tracked_path == 'TEST_FILE_FILE':
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

        except AssertionError as error:
            print(f'FAILED TEST: {tracked_path}')
            print(error)

def test_result_everything_possible_unlinked(original_dir_test, destination_dir_test, tracked_paths):

    print('*** test_result_everything_possible_unlinked ***')

    for tracked_path in tracked_paths:

        tracked_path_home = os.path.join(original_dir_test, tracked_path)
        tracked_path_backup = os.path.join(destination_dir_test, tracked_path)

        try:
            if tracked_path == 'TEST_NO_FILE':
                assert (not os.path.exists(tracked_path_home))
                assert (os.path.exists(tracked_path_backup))
            elif tracked_path == 'TEST_SYM_WRONG_FILE':
                assert (os.path.islink(tracked_path_home))
                assert (not os.readlink(tracked_path_home) == tracked_path_backup)
                assert (os.path.exists(tracked_path_backup))
            elif tracked_path == 'TEST_DIR_FILE':
                assert (os.path.isdir(tracked_path_home))
                assert (os.path.exists(tracked_path_backup))
            elif tracked_path == 'TEST_FILE_FILE':
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
            elif (tracked_path == 'TEST_DIR_NO'
                    or tracked_path == 'TEST_SYM_RIGHT_DIR'):
                assert (os.path.isdir(tracked_path_home))
                assert (not os.path.exists(tracked_path_backup))
                assert (not os.path.islink(tracked_path_backup))
            elif (tracked_path == 'TEST_FILE_NO'
                    or tracked_path == 'TEST_SYM_RIGHT_FILE'):
                assert (os.path.isfile(tracked_path_home))
                assert (not os.path.exists(tracked_path_backup))
                assert (not os.path.islink(tracked_path_backup))
            else:
                raise Exception('Unknown test tracked path!')

        except AssertionError as error:
            print(f'FAILED TEST: {tracked_path}')
            print(error)


def test_result_unlink(original_dir_test, destination_dir_test, tracked_paths):

    for tracked_path in tracked_paths:

        tracked_path_home = os.path.join(original_dir_test, tracked_path)
        tracked_path_backup = os.path.join(destination_dir_test, tracked_path)

        try:
            if tracked_path == 'TEST_NO_FILE':
                assert (not os.path.exists(tracked_path_home))
                assert (os.path.exists(tracked_path_backup))
            elif tracked_path == 'TEST_SYM_RIGHT_FILE':
                assert (os.path.isfile(tracked_path_home))
                assert (not os.path.exists(tracked_path_backup))
                assert (not os.path.islink(tracked_path_backup))
            elif tracked_path == 'TEST_SYM_RIGHT_DIR':
                assert (os.path.isdir(tracked_path_home))
                assert (not os.path.exists(tracked_path_backup))
                assert (not os.path.islink(tracked_path_backup))
                # pass
            elif tracked_path == 'TEST_SYM_WRONG_FILE':
                assert (os.path.islink(tracked_path_home))
                assert (not os.readlink(tracked_path_home) == tracked_path_backup)
                assert (os.path.exists(tracked_path_backup))
            elif tracked_path == 'TEST_DIR_FILE':
                assert (os.path.isdir(tracked_path_home))
                assert (os.path.exists(tracked_path_backup))
            elif tracked_path == 'TEST_FILE_FILE':
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

def test_pathlinker(test_name, run_script_lambda, test_result_function_dict):

    print(f'### {test_name}')

    # Directories for testing
    CURR_DIR = os.path.expandvars('$PWD')
    TEST_DIR = os.path.join(CURR_DIR, 'pathlinker_test_dir')

    ORIGINAL_DIR = os.path.join(TEST_DIR, 'original_dir')
    ORIGINAL_DIR_TEST_1 = os.path.join(TEST_DIR, 'original_dir_test_1')
    ORIGINAL_DIR_TEST_2 = os.path.join(TEST_DIR, 'original_dir_test_2')
    DESTINATION_DIR = os.path.join(TEST_DIR, 'destination_dir')
    DESTINATION_DIR_TEST_1 = os.path.join(TEST_DIR, 'destination_dir_test_1')
    DESTINATION_DIR_TEST_2 = os.path.join(TEST_DIR, 'destination_dir_test_2')

    # Test files
    TRACKED_PATHS = [
        'TEST_NO_FILE',
        'TEST_SYM_RIGHT_FILE',
        'TEST_SYM_RIGHT_DIR',
        'TEST_SYM_WRONG_FILE',
        'TEST_DIR_FILE',
        'TEST_FILE_FILE',
        'TEST_NO_NO',
        'TEST_SYM_NO',
        'TEST_DIR_NO',
        'TEST_FILE_NO'
    ]

    SETTINGS_FILE = os.path.join(TEST_DIR, 'pathlinker.json')
    SETTINGS_FILE_TEST = os.path.join(TEST_DIR, 'pathlinker_test.json')

    # Setup testing environment
    
    # Make test copies
    shutil.copytree(ORIGINAL_DIR, ORIGINAL_DIR_TEST_1, symlinks=True)
    shutil.copytree(ORIGINAL_DIR, ORIGINAL_DIR_TEST_2, symlinks=True)

    shutil.copytree(DESTINATION_DIR, DESTINATION_DIR_TEST_1, symlinks=True)
    shutil.copytree(DESTINATION_DIR, DESTINATION_DIR_TEST_2, symlinks=True)

    shutil.copyfile(SETTINGS_FILE, SETTINGS_FILE_TEST)

    # Add test symlink
    os.symlink(os.path.join(DESTINATION_DIR_TEST_1, 'TEST_SYM_RIGHT_FILE'), os.path.join(ORIGINAL_DIR_TEST_1, 'TEST_SYM_RIGHT_FILE'))
    os.symlink(os.path.join(DESTINATION_DIR_TEST_1, 'TEST_SYM_RIGHT_DIR'), os.path.join(ORIGINAL_DIR_TEST_1, 'TEST_SYM_RIGHT_DIR'))

    os.symlink(os.path.join(DESTINATION_DIR_TEST_2, 'TEST_SYM_RIGHT_FILE'), os.path.join(ORIGINAL_DIR_TEST_2, 'TEST_SYM_RIGHT_FILE'))
    os.symlink(os.path.join(DESTINATION_DIR_TEST_2, 'TEST_SYM_RIGHT_DIR'), os.path.join(ORIGINAL_DIR_TEST_2, 'TEST_SYM_RIGHT_DIR'))

    # Setup pathlink.json settings
    with open(SETTINGS_FILE_TEST, 'r') as fp:
        settings_content = json.load(fp)

    settings_content['test_settings_id_1']['original_dir'] = ORIGINAL_DIR_TEST_1
    settings_content['test_settings_id_1']['destination_dir'] = DESTINATION_DIR_TEST_1

    settings_content['test_settings_id_2']['original_dir'] = ORIGINAL_DIR_TEST_2
    settings_content['test_settings_id_2']['destination_dir'] = DESTINATION_DIR_TEST_2

    with open(SETTINGS_FILE_TEST, 'w') as fp:
        json.dump(settings_content, fp, indent=4, sort_keys=True)

    try:
        run_script_lambda(SETTINGS_FILE_TEST)
    except Exception as e:
        print(f'pathlinker script error: {e}')

    for settings_id, test_result_function in test_result_function_dict.items():
        print(f' Testing: {settings_id}')
        test_result_function(settings_content[settings_id]['original_dir'], 
            settings_content[settings_id]['destination_dir'], TRACKED_PATHS)

    # Clean testing dirs
    shutil.rmtree(ORIGINAL_DIR_TEST_1)
    shutil.rmtree(ORIGINAL_DIR_TEST_2)

    shutil.rmtree(DESTINATION_DIR_TEST_1)
    shutil.rmtree(DESTINATION_DIR_TEST_2)

    os.remove(SETTINGS_FILE_TEST)

test_pathlinker('TEST 1 (mode="link" settings_id="*" execute_linking=True)', 
    lambda settings_file: pathlinker.pathlink(settings_file, mode='link', settings_id='*', execute_linking=True, automatic_yes=True, silent=True),
    {
        "test_settings_id_1" : test_result_everything_possible_linked,
        "test_settings_id_2" : test_result_everything_possible_linked    
    })

test_pathlinker('TEST 2 (mode="link" settings_id="test_settings_id_1" execute_linking=True)', 
    lambda settings_file: pathlinker.pathlink(settings_file, mode='link', settings_id='test_settings_id_1', execute_linking=True, automatic_yes=True, silent=True),
    {
        "test_settings_id_1" : test_result_everything_possible_linked,
        "test_settings_id_2" : test_result_nothing_gets_changed
    })

test_pathlinker('TEST 3 (mode="link" settings_id="*" execute_linking=False)', 
    lambda settings_file: pathlinker.pathlink(settings_file, mode='link', settings_id='*', execute_linking=False, silent=True),
    {
        "test_settings_id_1" : test_result_nothing_gets_changed,
        "test_settings_id_2" : test_result_nothing_gets_changed    
    })

test_pathlinker('TEST 4 (mode="unlink" settings_id="*" execute_linking=True)', 
    lambda settings_file: pathlinker.pathlink(settings_file, mode='unlink', settings_id='*', execute_linking=True, automatic_yes=True, silent=True),
    {
        "test_settings_id_1" : test_result_everything_possible_unlinked,
        "test_settings_id_2" : test_result_everything_possible_unlinked
    })

test_pathlinker('TEST 5 (mode="unlink" settings_id="test_settings_id_2" execute_linking=True)', 
    lambda settings_file: pathlinker.pathlink(settings_file, mode='unlink', settings_id='test_settings_id_2', execute_linking=True, automatic_yes=True, silent=True),
    {
        "test_settings_id_1" : test_result_nothing_gets_changed,
        "test_settings_id_2" : test_result_everything_possible_unlinked
    })

test_pathlinker('TEST 6 (mode="unlink" settings_id="*" execute_linking=False)', 
    lambda settings_file: pathlinker.pathlink(settings_file, mode='unlink', settings_id='*', execute_linking=False, silent=True),
    {
        "test_settings_id_1" : test_result_nothing_gets_changed,
        "test_settings_id_2" : test_result_nothing_gets_changed
    })

