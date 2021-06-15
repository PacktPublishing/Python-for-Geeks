#pipeline2.py: Separate subject with grade from a PCollection
import apache_beam as beam

def my_format(sub, marks):
    yield '{}\t{}'.format(sub,marks)

with beam.Pipeline() as pipeline:
  plants = (
      pipeline
      | 'Subjects' >> beam.Create([
      ('English','A'),
      ('Maths', 'B+'),
      ('Science', 'A-'),
      ('French', 'A'),
      ('Arts', 'A+'),
      ])
      | 'Format subjects with marks' >> beam.FlatMapTuple(my_format)
      | beam.Map(print))