from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when

def get_product_category_pairs_and_products_without_categories(products_df, categories_df, product_categories_df):
    product_categories_joined = products_df.join(product_categories_df, on="product_id", how="left")

    product_category_names = product_categories_joined.join(categories_df, on="category_id", how="left") \
        .select(col("product_name"), col("category_name"))

    products_without_categories = product_category_names.where(col("category_name").isNull()) \
        .select(col("product_name"), lit(None).alias("category_name"))

    products_without_categories = products_without_categories.withColumn("no_category", lit(True))

    product_category_names = product_category_names.where(col("category_name").isNotNull()) \
        .withColumn("no_category", lit(False))

    result_df = product_category_names.unionByName(products_without_categories, allowMissingColumns=True)

    return result_df

def main():
    spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()

    products_data = [
        (1, "Milk"),
        (2, "Chocolate"),
        (3, "Banana"),
        (4, "Orange")
    ]
    categories_data = [
        (101, "Category First"),
        (102, "Category Second")
    ]
    product_categories_data = [
        (1, 1001),
        (1, 1002),
        (2, 1001)
    ]

    # Создание DataFrames
    products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])
    categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])
    product_categories_df = spark.createDataFrame(product_categories_data, ["product_id", "category_id"])

    result_df = get_product_category_pairs_and_products_without_categories(products_df, categories_df, product_categories_df)

    result_df.show()

    spark.stop()

main()