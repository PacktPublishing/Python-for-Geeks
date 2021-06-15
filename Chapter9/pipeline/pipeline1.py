#pipeline1.py: Separate strings from a PCollection
import apache_beam as beam

with beam.Pipeline() as pipeline:
  plants = (
      pipeline
      | 'Subjects' >> beam.Create([
          'English Maths Science',
          'French Arts',
      ])
      | 'Split subjects' >> beam.FlatMap(str.split)
      | beam.Map(print))