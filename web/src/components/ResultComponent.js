import React from 'react';
import Col from 'react-bootstrap/Col';
import { FaThumbsUp, FaThumbsDown } from 'react-icons/fa';

const ResultComponent = ({ predictions }) => {
  return (
    <Col md={6} className="text-center">
      <div className="result-section">
        <div class="sentiment-indicator">
          <h5 id="result">
            Your Text Sentiment is: {predictions.pred_sentiment === 1 ? (
              <div>
                <FaThumbsUp /> Positive
              </div>
            ) : (
              <div>
                <FaThumbsDown /> Negative
              </div>
            )}
          </h5>
        </div>
      </div>
      <h5 id="result">Your Personality Traits:</h5>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Prediction</th>
            <th scope="col">Trait Score</th>
            <th scope="col">Normalized Score</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Openness</th>
            <td>{predictions.pred_sOPN}</td>
            <td>{predictions.pred_sOPN_normalized}</td>
          </tr>
          <tr>
            <th scope="row">Conscientiousness</th>
            <td>{predictions.pred_sCON}</td>
            <td>{predictions.pred_sCON_normalized}</td>
          </tr>
          <tr>
            <th scope="row">Extraversion</th>
            <td>{predictions.pred_sEXT}</td>
            <td>{predictions.pred_sEXT_normalized}</td>
          </tr>
          <tr>
            <th scope="row">Agreeableness</th>
            <td>{predictions.pred_sAGR}</td>
            <td>{predictions.pred_sAGR_normalized}</td>
          </tr>
          <tr>
            <th scope="row">Neuroticism</th>
            <td>{predictions.pred_sNEU}</td>
            <td>{predictions.pred_sNEU_normalized}</td>
          </tr>
        </tbody>
      </table>
    </Col>
  );
}

export default ResultComponent;
