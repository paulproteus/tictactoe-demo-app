## About this codebase

This is an example of how to write an API using Django views to
implement a public tic-tac-toe service.

For now, please don't copy it or run it yourself unless you have my
permission. Lincoln and Drew have my permission!

## Overview and structure

- This is a Django project, with one Django app embedded.

- If you read the Django project's settings, you'll see there is no
  database and most default features of Django such as CSRF protection
  and the ability to locate templates have been disabled. Tread
  carefully, and feel free to enable Django features as-needed.

- As you edit the codebase, run the tests with:

```
bash run_tests.sh
```

- Most code changes will be done in `tttproject/tttapp/gamelogic.py`.

## Tic-tac-toe implementation notes

- This implementation treats a board state as string.

- It uses minimax to find the best move to take.

## Data validation notes

- Data is validated directly in the Django view function.
