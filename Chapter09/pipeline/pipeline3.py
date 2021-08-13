#pipeline3.py: Read data from a file and give results back to another file
import apache_beam as beam
from apache_beam.io import WriteToText, ReadFromText

with beam.Pipeline() as pipeline:
    lines = pipeline | ReadFromText('sample1.txt')

    subjects = (
      lines
      | 'Subjects' >> beam.FlatMap(str.split))

    subjects | WriteToText(file_path_prefix='subjects',
                           file_name_suffix='.txt',
                           shard_name_template='')