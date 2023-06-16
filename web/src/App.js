import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import Row from 'react-bootstrap/Row';

import FormComponent from './components/FormComponent';
import ProgressBarComponent from './components/ProgressBarComponent';
import ResultComponent from './components/ResultComponent';
import RadarChartComponent from './components/RadarChartComponent';
import ContainerComponent from './layout/ContainerComponent';
import GuideComponent from './components/GuideComponent';
import { postBigFiveData, postPreviewData } from './actions/api';

import './App.css';

const App = () => {
  // State for the input
  const [content, setContent] = useState('');
  // State for the prediction data
  const [predictions, setPredictions] = useState(false);
  // State for the error message
  const [error, setError] = useState('');
  // State for the loading state
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const text = e.target.value;
    // Update the content state with the input text
    setContent(text);
  }

  const handlePredict = async (e) => {
    e.preventDefault();
    if (!content) {
      setError('Please enter some statements.');
      return;
    }
    // Set loading state to true
    setLoading(true);
    setError('');
    try {
      // Call the API function to get the prediction data
      const data = await postBigFiveData(content);
      // Update the predictions state with the fetched data
      setPredictions(data);
    } catch (error) {
      setError(error.message);
    } finally {
      // Set loading state to false
      setLoading(false);
    }
  }

  const handlePreview = async (e) => {
    e.preventDefault();
    if (!content) {
      setError('Please enter some statements.');
      return;
    }

    setLoading(true);
    setError('');
    try {
      const data = await postPreviewData(content);
      setPredictions(data);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <ContainerComponent>
      <div>
        <h2 className="title">Psychology Insights</h2>
      </div>
      <GuideComponent />
      <div className="content">
        <FormComponent
          content={content}
          error={error}
          loading={loading}
          handleChange={handleChange}
          handlePreview={handlePreview}
          handlePredict={handlePredict}
        />

        {loading && <ProgressBarComponent />}

        {predictions && (
          <Row className="result-container">
            <ResultComponent predictions={predictions} />
            <RadarChartComponent predictions={predictions} />
          </Row>
        )}
      </div>
    </ContainerComponent>
  );
}

export default App;
