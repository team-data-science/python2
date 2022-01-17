import pandas as pd
# load a csv file
e_commerce_data_path_csv = "./data/data.csv"
e_commerce_csv_df = pd.read_csv(
    e_commerce_data_path_csv,  encoding='unicode_escape', nrows=1000)
# show columns
e_commerce_csv_df.columns
# > Index(['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
# >        'UnitPrice', 'CustomerID', 'Country'],
# >       dtype='object')

# show types
e_commerce_csv_df.dtypes
# > InvoiceNo       object
# > StockCode       object
# > Description     object
# > Quantity         int64
# > InvoiceDate     object
# > UnitPrice      float64
# > CustomerID     float64
# > Country         object
# > dtype: object

# change types
e_commerce_csv_df = e_commerce_csv_df.convert_dtypes()
# New dtypes
e_commerce_csv_df.dtypes
# > InvoiceNo       string
# > StockCode       string
# > Description     string
# > Quantity         Int64
# > InvoiceDate     string
# > UnitPrice      Float64
# > CustomerID       Int64
# > Country         string
# > dtype: object

# Cast a pandas object to a specified dtype dtype via dictionary, quantity from int64 to float64, and customerID from int64 to flat64. This
# is just a dummy example, and I am not telling you that converting customerid to float is a smart move:)

temp_dtype_change_df = e_commerce_csv_df.astype(
    {'Quantity': 'float64',
     'CustomerID': 'float64'
     }
)
temp_dtype_change_df.dtypes
# > InvoiceNo       string
# > StockCode       string
# > Description     string
# > Quantity       float64
# > InvoiceDate     string
# > UnitPrice      Float64
# > CustomerID     float64
# > Country         string
# > dtype: object

# load json

e_commerce_data_path_json = "./data/data_subset.json"
e_commerce_json_df = pd.read_json(
    e_commerce_data_path_json,  encoding='unicode_escape')

# join the csv and the json to a new dataframe
len(e_commerce_csv_df) + len(e_commerce_json_df)
# > 1004

e_commerce_appended_df = e_commerce_csv_df.append(e_commerce_json_df)
e_commerce_appended_df
# >     InvoiceNo StockCode                          Description  Quantity         InvoiceDate UnitPrice  CustomerID         Country
# > 0      536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6 2010-12-01 08:26:00      2.55       17850  United Kingdom
# > 1      536365     71053                  WHITE METAL LANTERN         6 2010-12-01 08:26:00      3.39       17850  United Kingdom
# > 2      536365    84406B       CREAM CUPID HEARTS COAT HANGER         8 2010-12-01 08:26:00      2.75       17850  United Kingdom
# > 3      536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6 2010-12-01 08:26:00      3.39       17850  United Kingdom
# > 4      536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6 2010-12-01 08:26:00      3.39       17850  United Kingdom
# > ..        ...       ...                                  ...       ...                 ...       ...         ...             ...
# > 999    536520     21358           TOAST ITS - HAPPY BIRTHDAY         2 2010-12-01 12:43:00      1.25       14729  United Kingdom
# > 0      536370     22492               MINI PAINT SET VINTAGE        36 2010-12-01 08:45:00      0.65       12583          France
# > 1      536372     22632            HAND WARMER RED POLKA DOT         6 2010-12-01 09:01:00      1.85       17850  United Kingdom
# > 2      536389     22727             ALARM CLOCK BAKELIKE RED         4 2010-12-01 10:03:00      3.75       12431       Australia
# > 3      562106     22993         SET OF 4 PANTRY JELLY MOULDS         1 2011-08-02 15:19:00      1.25       14076  United Kingdom
# >
# > [1004 rows x 8 columns]
len(e_commerce_appended_df)
# > 1004

# print out first few rows of the dataframe
e_commerce_appended_df.head(10)
# >   InvoiceNo StockCode                          Description  Quantity     InvoiceDate UnitPrice  CustomerID         Country
# > 0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6  12/1/2010 8:26      2.55       17850  United Kingdom
# > 1    536365     71053                  WHITE METAL LANTERN         6  12/1/2010 8:26      3.39       17850  United Kingdom
# > 2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8  12/1/2010 8:26      2.75       17850  United Kingdom
# > 3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6  12/1/2010 8:26      3.39       17850  United Kingdom
# > 4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6  12/1/2010 8:26      3.39       17850  United Kingdom
# > 5    536365     22752         SET 7 BABUSHKA NESTING BOXES         2  12/1/2010 8:26      7.65       17850  United Kingdom
# > 6    536365     21730    GLASS STAR FROSTED T-LIGHT HOLDER         6  12/1/2010 8:26      4.25       17850  United Kingdom
# > 7    536366     22633               HAND WARMER UNION JACK         6  12/1/2010 8:28      1.85       17850  United Kingdom
# > 8    536366     22632            HAND WARMER RED POLKA DOT         6  12/1/2010 8:28      1.85       17850  United Kingdom
# > 9    536367     84879        ASSORTED COLOUR BIRD ORNAMENT        32  12/1/2010 8:34      1.69       13047  United Kingdom

# do a lambda to change of the timestamp from / to epoch
# before
e_commerce_appended_df.dtypes
# > InvoiceNo      object
# > StockCode      object
# > Description    object
# > Quantity        Int64
# > InvoiceDate    object
# > UnitPrice      object
# > CustomerID      Int64
# > Country        object
# > dtype: object

e_commerce_appended_df['InvoiceDate'] = pd.to_datetime(
    e_commerce_appended_df['InvoiceDate'])

# after
e_commerce_appended_df.dtypes
# > InvoiceNo              object
# > StockCode              object
# > Description            object
# > Quantity                Int64
# > InvoiceDate    datetime64[ns]
# > UnitPrice              object
# > CustomerID              Int64
# > Country                object
# > dtype: object

# Filter out two columns "Country" and "Quantity"
e_commerce_appended_df.columns
# > Index(['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
# >        'UnitPrice', 'CustomerID', 'Country'],
# >       dtype='object')

e_commerce_appended_df = e_commerce_appended_df.drop(
    ["Country", "Quantity"], axis="columns")

e_commerce_appended_df.columns
# > Index(['InvoiceNo', 'StockCode', 'Description', 'InvoiceDate', 'UnitPrice',
# >        'CustomerID'],
# >       dtype='object')

# normalize the dataframe
# normalize a Pandas Column with Maximum Absolute Scaling using Pandas
e_commerce_csv_df.head(5)
# >   InvoiceNo StockCode                          Description  Quantity     InvoiceDate  UnitPrice  CustomerID         Country
# > 0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6  12/1/2010 8:26       2.55       17850  United Kingdom
# > 1    536365     71053                  WHITE METAL LANTERN         6  12/1/2010 8:26       3.39       17850  United Kingdom
# > 2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8  12/1/2010 8:26       2.75       17850  United Kingdom
# > 3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6  12/1/2010 8:26       3.39       17850  United Kingdom
# > 4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6  12/1/2010 8:26       3.39       17850  United Kingdom

cols_to_normalize = ["Quantity", "UnitPrice"]


def absolute_maximum_scale(series):
    return series / series.abs().max()

for column in cols_to_normalize:
    e_commerce_csv_df[column] = absolute_maximum_scale(
            e_commerce_csv_df[column])


e_commerce_csv_df.head(5)
# >   InvoiceNo StockCode                          Description  Quantity     InvoiceDate  UnitPrice  CustomerID         Country
# > 0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER      0.01  12/1/2010 8:26   0.015455       17850  United Kingdom
# > 1    536365     71053                  WHITE METAL LANTERN      0.01  12/1/2010 8:26   0.020545       17850  United Kingdom
# > 2    536365    84406B       CREAM CUPID HEARTS COAT HANGER  0.013333  12/1/2010 8:26   0.016667       17850  United Kingdom
# > 3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE      0.01  12/1/2010 8:26   0.020545       17850  United Kingdom
# > 4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.      0.01  12/1/2010 8:26   0.020545       17850  United Kingdom

# pivot the normalized dataframe

e_commerce_csv_df["Country"].unique()
# > <StringArray>
# > ['United Kingdom', 'France', 'Australia', 'Netherlands']
# > Length: 4, dtype: string

e_commerce_csv_df["unique_id"] = e_commerce_csv_df["InvoiceNo"] + \
    e_commerce_csv_df["StockCode"] + \
    e_commerce_csv_df["CustomerID"].astype("str")

e_commerce_pivoted = (e_commerce_csv_df
                      .filter(items=["unique_id", "UnitPrice", "Country"])
                      .pivot_table(
                          index="unique_id",
                          columns="Country",  # Column(s) we want to pivot.
                          # Column with values that we want to have in our new pivoted columns.
                          values="UnitPrice",
                          # Even if there is not aggregation we need to provide aggregation funciton.
                          aggfunc="mean"
                      )
                      .reset_index()
                      )
e_commerce_pivoted
# > Country          unique_id  Australia  France  Netherlands  United Kingdom
# > 0         5363652173017850       <NA>    <NA>         <NA>        0.025758
# > 1         5363652275217850       <NA>    <NA>         <NA>        0.046364
# > 2         5363657105317850       <NA>    <NA>         <NA>        0.020545
# > 3        53636584029E17850       <NA>    <NA>         <NA>        0.020545
# > 4        53636584029G17850       <NA>    <NA>         <NA>        0.020545
# > ..                     ...        ...     ...          ...             ...
# > 940      C5363912198417548       <NA>    <NA>         <NA>        0.001758
# > 941      C5363912255317548       <NA>    <NA>         <NA>            0.01
# > 942      C5363912255617548       <NA>    <NA>         <NA>            0.01
# > 943      C5363912255717548       <NA>    <NA>         <NA>            0.01
# > 944      C5365062296017897       <NA>    <NA>         <NA>        0.025758
# >
# > [945 rows x 5 columns]

# store dataframe as parquet file
e_commerce_pivoted.to_parquet('./data/e_commerce_pivoted.parquet.gzip',
                              compression='gzip')
# > None

# read parquet file

pd.read_parquet(
    './data/e_commerce_pivoted.parquet.gzip')
# > Country          unique_id  Australia  France  Netherlands  United Kingdom
# > 0         5363652173017850       <NA>    <NA>         <NA>        0.025758
# > 1         5363652275217850       <NA>    <NA>         <NA>        0.046364
# > 2         5363657105317850       <NA>    <NA>         <NA>        0.020545
# > 3        53636584029E17850       <NA>    <NA>         <NA>        0.020545
# > 4        53636584029G17850       <NA>    <NA>         <NA>        0.020545
# > ..                     ...        ...     ...          ...             ...
# > 940      C5363912198417548       <NA>    <NA>         <NA>        0.001758
# > 941      C5363912255317548       <NA>    <NA>         <NA>            0.01
# > 942      C5363912255617548       <NA>    <NA>         <NA>            0.01
# > 943      C5363912255717548       <NA>    <NA>         <NA>            0.01
# > 944      C5365062296017897       <NA>    <NA>         <NA>        0.025758
# >
# > [945 rows x 5 columns]
