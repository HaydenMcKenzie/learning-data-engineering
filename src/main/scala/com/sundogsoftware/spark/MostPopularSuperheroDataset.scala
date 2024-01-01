package com.sundogsoftware.spark

import org.apache.log4j._
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types.{IntegerType, StringType, StructType}

/** Find the superhero with the most co-appearances. */
object MostPopularSuperheroDataset {

  case class SuperHeroNames(id: Int, name: String)
  case class SuperHero(value: String)
 
  /** Our main function where the action happens */
  def main(args: Array[String]) {
   
    // Set the log level to only print errors
    Logger.getLogger("org").setLevel(Level.ERROR)

    // Create a SparkSession using every core of the local machine
    val spark = SparkSession
      .builder
      .appName("MostPopularSuperhero")
      .master("local[*]")
      .getOrCreate()

    // Create schema when reading Marvel-names.txt
    val superHeroNamesSchema = new StructType()
      .add("id", IntegerType, nullable = true)
      .add("name", StringType, nullable = true)

    // Build up a hero ID -> name Dataset
    import spark.implicits._
    val names = spark.read
      .schema(superHeroNamesSchema)
      .option("sep", " ")
      .csv("data/Marvel-names.txt")
      .as[SuperHeroNames]

    // No need to write a schema as there is only one line
    val lines = spark.read
      .text("data/Marvel-graph.txt")
      .as[SuperHero]

    val connections = lines
      .withColumn("id", split(col("value"), " ")(0)) // The doesnt have any rows. This creates a row call "id" and adds only the first element to it
      .withColumn("connections", size(split(col("value"), " ")) - 1) // Makes another row, turns all into an array and minuses 1 from the total number
      .groupBy("id").agg(sum("connections").alias("connections")) // Counts all elements in array corresponding to "id" column

    val mostPopular = connections
        .sort($"connections".desc) // sort by descending order
        .first() // takes the first result

    val mostPopularName = names
      .filter($"id" === mostPopular(0))
      .select("name")
      .first() // links the ID with the name of the mostPopular superhero

    println(s"${mostPopularName(0)} is the most popular superhero with ${mostPopular(1)} co-appearances.")
  }
}
