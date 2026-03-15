## Descrizione del progetto

Questo progetto implementa un sistema completo per il **deploy e il monitoraggio di un modello di Sentiment Analysis** applicato alle recensioni di prodotti in lingua inglese.

L'obiettivo è simulare un contesto aziendale in cui una piattaforma di e-commerce riceve migliaia di recensioni e necessita di un sistema automatizzato per analizzarne il sentiment (positivo o negativo).

Il sistema espone il modello tramite una **REST API**, implementa **monitoraggio delle prestazioni**, **test automatici** e una **pipeline CI/CD** per il deploy automatizzato.

---

## Tecnologie utilizzate

- Python
- FastAPI
- Scikit-learn
- Prometheus
- Grafana
- Docker
- Docker Compose
- Jenkins
- Pytest

---

## Struttura del progetto

```
sentiment-devops-project
│
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── model_loader.py
│   ├── monitoring.py
│   └── schemas.py
│
├── deployment
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── model
│   └── sentimentanalysismodel.pkl
│
├── monitoring
│   └── prometheus.yml
│
├── tests
│   └── test_api.py
│
├── training
│   └── training_model.py
│
├── Jenkinsfile
├── README.md
├── requirements.txt
│

```

---

## Funzionamento del sistema

Il sistema espone un servizio REST che permette di inviare una recensione e ottenere il sentiment analizzato dal modello.

Architettura semplificata: 
Client -> FastAPI API -> Modello Machine Learning -> Metriche Prometheus -> Grafana Dashboard


---

## Avvio dell'applicazione locale

L'applicazione è stata eseguita in ambiente locale utilizzando **Anaconda Prompt** con Python, versione 3.13, su sistema Windows.
Per avviare l'applicazione manualmente:

| Operazione | Comando |
|------------|--------|
| Avviare il server FastAPI | `uvicorn app.main:app --reload` |

Il server sarà disponibile su:

| Servizio | URL |
|---------|-----|
| API | http://127.0.0.1:8000 |
| Documentazione API | http://127.0.0.1:8000/docs |

---

## Endpoint disponibili

| Endpoint | Metodo | Descrizione |
|--------|------|-------------|
| `/health` | GET | Verifica lo stato dell'API e del modello |
| `/predict` | POST | Restituisce il sentiment di una recensione |
| `/metrics` | GET | Espone le metriche Prometheus |

## Metriche raccolte

- numero totale di richieste API
- numero di errori di predizione
- tempo di risposta delle richieste
- utilizzo della CPU
- utilizzo della memoria

Queste metriche possono essere raccolte da **Prometheus** e visualizzate tramite **Grafana**.

## Training del modello 

Il progetto include uno script di training per dimostrare come è stato generato il modello di Machine Learning.

| Operazione | Comando |
|------------|--------|
| Addestrare il modello | `python training/train_model.py` |

Lo script:

- utilizza **Scikit-learn**
- applica una pipeline con **CountVectorizer** e **Multinomial Naive Bayes**
- esegue una semplice valutazione del modello
- salva il modello addestrato nel file: model/sentimentanalysismodel.pkl

---

## Test automatici

I test sono implementati con **pytest**.

| Operazione | Comando |
|------------|--------|
| Eseguire tutti i test | `pytest` |

I test verificano:

- funzionamento endpoint `/health`
- funzionamento endpoint `/predict`
- gestione input non validi

---

## Containerizzazione con Docker

Il progetto include un **Dockerfile** per containerizzare l'applicazione.

| Operazione | Comando |
|------------|--------|
| Build dell'immagine Docker | `docker build -t sentiment-api -f deployment/Dockerfile .` |
| Avviare l'intero stack | `docker compose -f deployment/docker-compose.yml up -d` |

Il progetto include uno script di training per dimostrare come è stato generato il modello di Machine Learning.

| Operazione | Comando |
|------------|--------|
| Addestrare il modello | `python training/train_model.py` |

Lo stack Docker include:
- FastAPI API
- Prometheus
- Grafana

---

## CI/CD con Jenkins
Il progetto inlude un Jenkinsfile che definisce una pipeline CI/CD per automatizzare il processo di integrazione e deploy.
La pipeline prevede le seguenti fasi:

1. **Checkout del codice**
   Jenkins scarica automaticamente il repository del progetto.

2. **Installazione delle dipendenze**
   Viene installato l'ambiente Python e tutte le librerie presenti in `requirements.txt`.

3. **Esecuzione dei test**
   I test automatici vengono eseguiti tramite `pytest` per verificare il corretto funzionamento dell'applicazione.

4. **Build dell'immagine Docker**
   Se i test vengono superati, Jenkins costruisce l'immagine Docker dell'applicazione.

5. **Deploy**
   L'applicazione può essere distribuita tramite Docker Compose.

Questa pipeline consente di garantire che ogni modifica al codice venga testata e distribuita in modo automatico e controllato.

---

## Limitazioni del progetto
A causa di restrizioni amministrative sull'installazione di software sul mio computer (aziendale), **Docker e Jenkins non sono stati eseguiti direttamente in ambiente locale**. Tuttavia, i file di configurazione necessari per il deploy e il monitoraggio sono stati preparati e strutturati coerentemente con l'applicazione sviluppata e testata.

---

## Conclusioni
Questo progetto dimostra come:

- esporre un modello di Machine Learning tramite API
- implementare test automatici per garantire la qualità del codice
- monitorare le prestazioni di un servizio tramite Prometheus
- visualizzare metriche tramite Grafana
- containerizzare un'applicazione con Docker
- definire una pipeline CI/CD per automatizzare il processo di integrazione e deploy