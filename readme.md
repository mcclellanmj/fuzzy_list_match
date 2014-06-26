Purpose
=======
This utility is used for comparing two lists to find things that are in both lists.  

Usage
=====
list_search.py [--threshold=n] first_file second_file

Threshold will set how close a match has to be before it will print, should be a number from 0-100

The results will be printed as
Found match on ITEM_FROM_LIST_ONE
- ITEM_FROM_LIST_TWO (CLOSENESS_OF_MATCH)
- OTHER_ITEM_FROM_LIST_TWO (CLOSENESS_OF_MATCH)