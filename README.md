# Advanced-ML-Task
                                                                TASK 1: NEWS TOPIC CLASSIFIER Using BERT
OBJECTIVE:Fine-tune a transformer model(e.g. BERT) to classify news headlines into topic categories.
DATASET USED: AG News Dataset 'uci-news-aggregator.csv' (Hugging Face Datasets).
MODEL USED:Distilbert-base-uncased (using Hugging Face Transformers).
MODEL EVALUATION:Evaluated the model using prediction accuracy and evaluated the predicted classifier.
METHODOLOGY/APPROACH:First imported libraries(transformers,torch,scikit-learn)tokenized and preprocessed the dataset;After applying model which is 'bert-base-uncased' fine tuned the model by saving the model as './fine_tune_model' using hugging face transformers ; then I evaluated the model by prediction/confidence score check that if the ML code is predicting the news category right or wrong;whether the news is business related or Entertainment related or Science/Technology related or Health/Medical related then evaluated the model accuracy and in the nutshell succesfully deployed the model using Streamlit for live interaction.
KEY RESULTS OR OBSERVATIONS:I have learned by training the model using ML that how can we predict or classify the news topics by making the code only reading the texts and made the code in a sense that it will read the headline and then specify/identify that it belongs to which news topics but the matter of concern is that the dataset we will upload, we can make the predictions of that particular dataset only.
SKILLS GAINED:NLP using Transformers; Transfer learning & fine-tuning; Evaluation metrics for text classification; Lightweight model employment.
                                                                TASK 2:Context-Aware Chatbot Using Langchain
OBJECTIVE:Build a conversational chatbot that can remember context and retrieve external information during conversations.
DATASET USED:multilang.txt(I used the knowledge base document that I downloaded it from a website,you can choose either any internal document or wikipedia pages)
MODEL USED:Created chatbot using LangChain.
MODEL EVALUATION:Evaluated the model by the .txt file I have uploaded which is multilang.txt that when i am asking the questions based on the uploaded document which means a memory for a chatbot it is retrieving that context or not.
METHODOLOGY/APPROACH:Firstly,I trained the model by LangChain;implemented context memory for conversational history;retrieve answers from a vectorized document store; and in the last deployed the chatbot with Streamlit.
KEY RESULTS OR OBSERVATIONS:Trained the model in a way that chatbot will read the question that will be asked by anyone on their uploaded content and then it will try to give the answers that was fed in the chatbot memory and it is al done by coding.
SKILLS GAINED: Conversational AI development;Document embedding and vector search;Retrieval of external information;LLM integration and deployment.
                                                                TASK 3:Auto Tagging Support Tickets Using LLM
OBJECTIVE:Automatically tag support tickets into categories using a large language model(LLM).
DATASET USED:support_tickets_train.csv & support_tickets_test.csv(Free-text Support Ticket Dataset)
MODEL USED:Created Support ticket queries using LLM.
MODEL EVALUATION:Evaluated the model by predicting the output "the top 3 most probable tags per ticket" with their probablities of having these three categories.
METHODOLOGY/APPROACH:In the first place, I have imported libraries like torch ,transformers; Used fine_tuned_model; After applying model which is 'distilbert-base-uncased' fine tuned the model by saving the model as './fine_tune_model';compared zero-shot vs fine-tuned performance;applied few-shot learning techniques to improve accuracy;output top 3 most probable tags per ticket.
KEY RESULTS OR OBSERVATIONS:Training was done by me in a way that based on the queries( or FAQs) that will be the asked by the people to know about about the update of product or request about the new feature; the people will enter the support ticket text; It will be processsed and then the prediction is made by the code that it will belong to which support the client is requesting for and give the ticket which is suitable for it.


