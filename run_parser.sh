cat $1 |
    perl -pe 's/(^[A-Z ]+)\t/###C: $1\n/g' |
    python3 full_pipeline_stream.py --gpu --conf models_fi_tdt/pipelines.yaml parse_plaintext


