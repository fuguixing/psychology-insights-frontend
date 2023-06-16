import React from 'react';
import Col from 'react-bootstrap/Col';
import RadarChart from 'react-svg-radar-chart';
import 'react-svg-radar-chart/build/css/index.css';
import '../styles/RadarChart.css';

const RadarChartComponent = ({ predictions }) => {
  return (
    <Col md={6} className="text-center">
      <h5 id="result">Traits Radar Plot:</h5>
      <div className="radar-chart-container">
        <RadarChart
          captions={{
            Openness: 'Openness',
            Conscientiousness: 'Conscientiousness',
            Extraversion: 'Extraversion',
            Agreeableness: 'Agreeableness',
            Neuroticism: 'Neuroticism',
          }}
          data={[
            {
              data: {
                Openness: predictions.pred_sOPN_normalized,
                Conscientiousness: predictions.pred_sCON_normalized,
                Extraversion: predictions.pred_sEXT_normalized,
                Agreeableness: predictions.pred_sAGR_normalized,
                Neuroticism: predictions.pred_sNEU_normalized,
              },
              meta: { color: 'blue' },
            },
          ]}
          size={400}
        />
      </div>
    </Col>
  );
}

export default RadarChartComponent;
