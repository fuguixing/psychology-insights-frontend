import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import App from './App';
import { postBigFiveData, postPreviewData } from './actions/api';

jest.mock('./actions/api', () => ({
  postBigFiveData: jest.fn(),
}));

describe('App', () => {
  beforeEach(() => {
    postBigFiveData.mockReset();
  });

  test('handles predict button click and calls postBigFiveData', async () => {
    const mockPredictions = {
      // Mock response data for predictions
    };
    postBigFiveData.mockResolvedValue(mockPredictions);

    render(<App />);

    const textArea = screen.getByTestId('input-field');
    userEvent.type(textArea, 'Some test content');

    const predictButton = screen.getByRole('button', { name: 'Predict' });
    userEvent.click(predictButton);

    expect(postBigFiveData).toHaveBeenCalledTimes(1);
    expect(postBigFiveData).toHaveBeenCalledWith('Some test content');

    await screen.findByText('Predictions');

    expect(screen.queryByText('Loading')).not.toBeInTheDocument();
  });
});
