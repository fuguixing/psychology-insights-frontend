import React, {useState} from 'react';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

const FormComponent = ({ content, error, loading, flag, handleChange, handlePreview, handlePredict }) => {
  return (
    <Form>
      <Form.Group>
        <Form.Label htmlFor="input">Input Text:</Form.Label>
        <Form.Control
          as="textarea"
          rows={5}
          id="input"
          data-testid="input-field"
          onChange={handleChange}
          value={content}
          isInvalid={error !== ''}
        />
        {error && <Form.Control.Feedback type="invalid">{error}</Form.Control.Feedback>}
      </Form.Group>
      <div className="button-group">
        <Button
          type="submit"
          variant="success"
          disabled={loading}
          onClick={!loading ? handlePreview : null}
          data-testid="preview-button"
        >
          {loading ? 'Analyzing...' : 'Try It'}
        </Button>
        <Button
          type="submit"
          variant="success"
          disabled={flag}
          onClick={!loading ? handlePredict : null}
          data-testid="predict-button"
        >
          {loading ? 'Analyzing...' : 'Predict'}
        </Button>
      </div>
    </Form>
  );
}

export default FormComponent;
