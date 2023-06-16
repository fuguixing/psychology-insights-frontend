import React from 'react';
import Col from 'react-bootstrap/Col';
import ProgressBar from 'react-bootstrap/ProgressBar';

const ProgressBarComponent = () => {
  return (
    <Col md={12} className="text-center">
      <ProgressBar animated now={100} label="Results will be displayed below" />
    </Col>
  );
}

export default ProgressBarComponent;
