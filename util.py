import polars as pl

def multi_select_counts(data: pl.DataFrame, columns: list, mapping: dict = None):

    df_count = data.select(columns).unpivot( on = columns[1:], index = "#").drop_nulls().to_pandas()["value"]
    
    if mapping is not None:
        df_count = df_count.replace(mapping)

    return df_count.value_counts()

import math

def get_subplot_coords(index, num_rows, num_cols):
    """
    Calculates the 1-indexed row and column for a subplot grid based on a 0-indexed position.

    Args:
        index (int): The 0-indexed position of the plot (from 0 to total_plots - 1).
        num_rows (int): The total number of rows in the subplot grid.
        num_cols (int): The total number of columns in the subplot grid.

    Returns:
        tuple: A tuple (row, col) representing the 1-indexed row and column
               for plotly's add_trace method. Returns None if inputs are invalid
               or index is out of range.
    """
    # Input validation
    if not isinstance(index, int) or index < 0:
        print("Error: 'index' must be a non-negative integer.")
        return None
    if not isinstance(num_rows, int) or num_rows <= 0:
        print("Error: 'num_rows' must be a positive integer.")
        return None
    if not isinstance(num_cols, int) or num_cols <= 0:
        print("Error: 'num_cols' must be a positive integer.")
        return None

    total_plots = num_rows * num_cols

    if not (0 <= index < total_plots):
        print(f"Index out of range. For a {num_rows}x{num_cols} grid ({total_plots} plots), "
              f"please provide an index between 0 and {total_plots - 1}.")
        return None

    # Calculate 1-indexed row and column
    # The row is determined by how many full 'num_cols' segments the index has passed.
    row = (index // num_cols) + 1
    # The column is determined by the remainder when index is divided by 'num_cols'.
    col = (index % num_cols) + 1

    return (row, col)


def df_prop(df: pl.DataFrame, col_name: str, num_obs: int, print_output=True):

    prop = df.group_by(col_name).len().with_columns( (pl.col("len")/num_obs).alias("prop"))

    if print_output:
        print(col_name)
        
        print(prop)

        return

    return prop

def df_multiselect_prop(df: pl.DataFrame, col_names: list, num_obs: int):

    d = multi_select_counts(df, ["#"] + col_names).reset_index()
    d["prop"] = d["count"]/num_obs

    return d

def pre_post_comparison(df_pre: pl.DataFrame, df_post: pl.DataFrame, N_pre: int, N_post: int, column_pre: str, column_post: str, standardized_col: str, entry_mapping: dict):

    df_pre = df_pre.select(column_pre).with_columns(
        pl.col(column_pre).replace(entry_mapping).alias(standardized_col),
        pl.lit("Pre-Orientation").alias("When"),
        pl.lit(N_pre).alias("N")
    ).drop(column_pre)

    df_post = df_post.select(column_post).with_columns(
        pl.col(column_post).replace(entry_mapping).alias(standardized_col),
        pl.lit("Post-Orientation").alias("When"),
        pl.lit(N_post).alias("N")
    ).drop(column_post)

    df = pl.concat([df_pre, df_post])

    df = df.group_by(df.columns).len().drop_nulls().with_columns( (100*pl.col("len")/pl.col("N")).alias("Percentage")).sort(by = standardized_col)

    return df