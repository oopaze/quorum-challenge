## HOW TO RUN

If you already have `python` and `pip` installed, that's gonna be simple:

```bash
# you just need to install de dependencies
pip install -r conf/requirements.txt

# once it finishes, you can run:
python run.py
```

OBS: the python version used on this project was *3.10.8*. Also, I left some Jupyter Notebooks files inside `jupyter` folder. So if you want to see more about the cases. To run those files, you just need to call Jupyter into your terminal:

```bash
# calling jupyter notebook
jupyter notebook
# OBS: you also need to install dependencies
```

## Questions

1. Discuss your solution’s time complexity. What tradeoffs did you make?

  The time complexity of both functions is `O(n*m)`. For the `asign_oppose_and_support_bills_count` `n` will represent the number of **legislators** we have and `m` the number of **vote_results** we have. For the `get_bills_votes` we will have the same things, the only change is related to the `n` which now represents the number of **bills**.

  Since I just use it eventually, I had to use `for` to go into the **bills** and **legislators** list. But I think we have a way to solve it avoiding the use of `for` and solving this problem only using `pandas`.

2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?
  For the “Bill Voted On Date” I would just add a new filter such as `is_supporting` and `is_opposing` that we have.
  For the "Co-Sponsors", I would just create a new column based on the `co_sponsor_id` and use `apply` to help me create this.

3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?
  The input is not a problem in this case. Pandas can handle it very ease. If it comes as a database select or an online sheet, I will just need to change the method and the parameters of pandas who calls it.

  For example, in your case, I will just create `DateFrames` using the list passed instead or call the `read_csv` function that Pandas gives to me.

4. How long did you spend working on the assignment?
  3 hours for the implementation and 1 hour for the documentation.



