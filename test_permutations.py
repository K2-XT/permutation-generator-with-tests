import pytest

from permutation_generator import *

def describe_algorithm_generator_file():
    
    def describe_set_up_list():
        
        def it_takes_a_number_and_generates_a_list_of_numbers_in_between():
            assert set_up_list(3) == [1, 2, 3]
            assert set_up_list(5) == [1, 2, 3, 4, 5]
            assert set_up_list(9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def describe_find_less_than():

        def it_takes_a_list_and_finds_the_first_index_where_lhs_lessthan_rhs_from_right():
            testl = [5, 4, 3, 1, 2]
            assert find_less_than(testl) == 4
            testl = [5, 3, 4, 2, 1]
            assert find_less_than(testl) == 2
            testl = [3, 5, 2, 4, 1]
            assert find_less_than(testl) == 3
            testl = [3, 5, 4, 2, 1]
            assert find_less_than(testl) == 1

        def it_should_break_from_loop_and_return_0_if_list_is_sorted():
            testl = [5, 4, 3, 2, 1]
            assert find_less_than(testl) == 0 

    def describe_exchange_numbers():

        def it_takes_a_list_and_position_exchanges_left_of_position_for_smallest_right_number():
            testl = [1, 4, 3, 5, 2]
            assert exchange_numbers(testl, 3) == [1, 4, 5, 3, 2]
            testl = [1, 4, 3, 2]
            assert exchange_numbers(testl, 1) == [2, 4, 3, 1]

    def describe_split_list():
        
        def it_takes_a_list_and_a_position_and_splits_the_list_in_two():
            testl = [1, 2, 3, 4, 5]
            assert split_list(testl, 3) == ([1,2,3], [4,5])
            testl = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            assert split_list(testl, 6) == ([1,2,3,4,5,6], [7,8,9])
            testl = [1, 2, 3, 4, 5]
            assert split_list(testl, 1) == ([1], [2,3,4,5])

    def describe_reverse_end_and_concatenate():
        
        def it_takes_two_lists_and_reverses_the_second_list_then_joins_and_returns_one():
            testl1 = [1, 2, 3]
            testl2 = [4, 5, 6]
            assert reverse_end_and_concatenate(testl1, testl2) == [1, 2, 3, 6, 5, 4]
            testl1 = [1, 2, 3]
            testl2 = [4, 5, 6, 7, 8]
            assert reverse_end_and_concatenate(testl1, testl2) == [1, 2, 3, 8, 7, 6, 5, 4]
            testl1 = [1]
            testl2 = [4, 5, 6]
            assert reverse_end_and_concatenate(testl1, testl2) == [1, 6, 5, 4]

        def it_does_not_reverse_order_if_list_2_has_only_2_elements():
            testl1 = [5, 4, 7]
            testl2 = [2, 1]
            assert reverse_end_and_concatenate(testl1, testl2) == [5, 4, 7, 2, 1]
            testl1 = [5, 4, 7]
            testl2 = [6, 9]
            assert reverse_end_and_concatenate(testl1, testl2) == [5, 4, 7, 6, 9]
            testl1 = [5, 4, 7]
            testl2 = [57, 9]
            assert reverse_end_and_concatenate(testl1, testl2) == [5, 4, 7, 57, 9]
