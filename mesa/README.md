# MESA project files

We make available our MESA project files, forked from the existing test suite `star/test_suite/1M_pre_ms_to_wd`, for independent compilation and execution. The source of the original test suite, as well as the version of MESA we used to run our stellar evolution, was MESA release version 12778 and compiled with MESA SDK version 20.3.2.

The subdirectory includes
- custom inlists
- custom `history_columns.list` and `profile_columns.list`
- custom `rn`
- produced models (`.mod`) from our run
- produced `history.data` from our run

We note that the contents of `/LOGS` in this repository's top-level directory was copied from `1M_pre_ms_to_wd/LOGS_to_end_agb`.