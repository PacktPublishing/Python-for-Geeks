#pipeline4.py: Using argument for a pipeline
import re

import apache_beam as beam
import argparse
from apache_beam.io import WriteToText, ReadFromText
from apache_beam.options.pipeline_options import PipelineOptions

class WordParsingDoFn(beam.DoFn):
  def process(self, element):
    return re.findall(r'[\w\']+', element, re.UNICODE)

def run(argv=None, save_main_session=True):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        default='sample1.txt',
        help='Input file to process.')
    parser.add_argument(
        '--output',
        dest='output',
        default='subjects',
        help='Output file to write results to.')

    parser.add_argument(
        '--extension',
        dest='ext',
        default='.txt',
        help='Output file extension to use.')

    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_args.extend([
        '--runner=DirectRunner',
        '--job_name=demo-local-job',
    ])
    pipeline_options = PipelineOptions(pipeline_args)
    with beam.Pipeline(options=pipeline_options) as pipeline:
        lines = pipeline | ReadFromText(known_args.input)
        subjects = (
                lines
                | 'Subjects' >> beam.ParDo(WordParsingDoFn()).
                with_output_types(str))

        subjects | WriteToText(known_args.output, known_args.ext)

if __name__ == '__main__':
    run()
