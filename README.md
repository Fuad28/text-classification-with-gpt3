# text-classification-with-gpt3

Experiencing the GPT3 API and using it to build a spam classification classification project using [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset?resource=download)

[Source](https://www.linkedin.com/pulse/gpt-3-text-classifier-everyone-yarik-menchaca-resendiz/?trk=pulse-article_more-articles_related-content-card)

Commands run:

-   Add your openapi key to environment: export OPENAI_API_KEY=xxxx
-   Run a tool to prepare and validate data: openai tools fine_tunes.prepare_data -f training.jsonl -q
-   To train the model on the data: openai api fine_tunes.create -t "training_prepared_train.jsonl" -v "training_prepared_valid.jsonl" --compute_classification_metrics --classification_positive_class " ham" -m ada
-   To follow up the fine-tuning process: openai api fine_tunes.follow -i ft-K9zHrWrwzzpJSj4clmD8sc1N
