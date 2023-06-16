import json
import logging
import azure.functions as func
from .models import ModelFactory

def bigfive_handler(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Handling big five personality request.')
    if req.method == 'POST':
        try:
            req_body = req.get_json()
            tfidf = ModelFactory.get_model("tfidf_model.joblib")
            text_input = [req_body]
            X_input = tfidf.transform(text_input)
            
            OPN_model = ModelFactory.get_model("OPN_regression_model.joblib")
            CON_model = ModelFactory.get_model("CON_regression_model.joblib")
            EXT_model = ModelFactory.get_model("EXT_regression_model.joblib")
            AGR_model = ModelFactory.get_model("AGR_regression_model.joblib")
            NEU_model = ModelFactory.get_model("NEU_regression_model.joblib")
            SENTIMENT_model = ModelFactory.get_model("model_review.joblib")
            SENTIMENT_VEC_model = ModelFactory.get_model("vect_review.joblib")
            
            pred_sOPN = OPN_model.predict(X_input).reshape(1, -1)
            pred_sOPN_value = round(float(pred_sOPN.flatten()[0]), 2)
            
            pred_sCON = CON_model.predict(X_input).reshape(1, -1)
            pred_sCON_value = round(float(pred_sCON.flatten()[0]), 2)
            
            pred_sEXT = EXT_model.predict(X_input).reshape(1, -1)
            pred_sEXT_value = round(float(pred_sEXT.flatten()[0]), 2)
            
            pred_sAGR = AGR_model.predict(X_input).reshape(1, -1)
            pred_sAGR_value = round(float(pred_sAGR.flatten()[0]), 2)
            
            pred_sNEU = NEU_model.predict(X_input).reshape(1, -1)
            pred_sNEU_value = round(float(pred_sNEU.flatten()[0]), 2)
            
            min_value = min(pred_sOPN, pred_sCON, pred_sEXT, pred_sAGR, pred_sNEU)
            max_value = max(pred_sOPN, pred_sCON, pred_sEXT, pred_sAGR, pred_sNEU)
            
            scaled_min = 0.05
            scaled_max = 0.95
            
            pred_sOPN_normalized = (pred_sOPN - min_value) / (max_value - min_value) * (scaled_max - scaled_min) + scaled_min
            pred_sCON_normalized = (pred_sCON - min_value) / (max_value - min_value) * (scaled_max - scaled_min) + scaled_min
            pred_sEXT_normalized = (pred_sEXT - min_value) / (max_value - min_value) * (scaled_max - scaled_min) + scaled_min
            pred_sAGR_normalized = (pred_sAGR - min_value) / (max_value - min_value) * (scaled_max - scaled_min) + scaled_min
            pred_sNEU_normalized = (pred_sNEU - min_value) / (max_value - min_value) * (scaled_max - scaled_min) + scaled_min
            
            pred_sOPN_normalized = round(float(pred_sOPN_normalized.flatten()[0]), 2)
            pred_sCON_normalized = round(float(pred_sCON_normalized.flatten()[0]), 2)
            pred_sEXT_normalized = round(float(pred_sEXT_normalized.flatten()[0]), 2)
            pred_sAGR_normalized = round(float(pred_sAGR_normalized.flatten()[0]), 2)
            pred_sNEU_normalized = round(float(pred_sNEU_normalized.flatten()[0]), 2)
            
            bowTest = SENTIMENT_VEC_model.transform(text_input)
            predicted_sentiment = SENTIMENT_model.predict(bowTest)
            predicted_sentiment_value = round(float(predicted_sentiment.flatten()[0]), 2)
            
            prediction = {
                'pred_sOPN': pred_sOPN_value,
                'pred_sOPN_normalized': pred_sOPN_normalized,
                'pred_sCON': pred_sCON_value,
                'pred_sCON_normalized': pred_sCON_normalized,
                'pred_sEXT': pred_sEXT_value,
                'pred_sEXT_normalized': pred_sEXT_normalized,
                'pred_sAGR': pred_sAGR_value,
                'pred_sAGR_normalized': pred_sAGR_normalized,
                'pred_sNEU': pred_sNEU_value,
                'pred_sNEU_normalized': pred_sNEU_normalized,
                'pred_sentiment': predicted_sentiment_value
            }
            
            response_data = {
                "prediction": prediction
            }
            
            response_body = json.dumps(response_data)
            
            return func.HttpResponse(
                body=response_body,
                mimetype="application/json",
                status_code=200
            )
        
        except Exception as e:
            return func.HttpResponse(
                body=str(e),
                status_code=500
            )
    
    else:
        return func.HttpResponse(
            "Method Not Allowed",
            status_code=405
        )

def preview_handler(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Handling analysis request.')
    req_body = req.get_json()
    
    prediction = {
        'pred_sOPN': 4.23,
        'pred_sOPN_normalized': 0.95,
        'pred_sCON': 3.48,
        'pred_sCON_normalized': 0.47,
        'pred_sEXT': 3.16,
        'pred_sEXT_normalized': 0.25,
        'pred_sAGR': 3.73,
        'pred_sAGR_normalized': 0.64,
        'pred_sNEU': 2.82,
        'pred_sNEU_normalized': 0.12,
        'pred_sentiment': 1
    }
    
    response_data = {
        "prediction": prediction
    }
    
    response_body = json.dumps(response_data)
    
    return func.HttpResponse(
        body=response_body,
        mimetype="application/json",
        status_code=200
    )
