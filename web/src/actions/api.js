export const postBigFiveData = async (content) => {
  try {
    const res = await fetch("/api/bigfive", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(content)
    });
    const data = await res.json();
    return data.prediction;
  } catch (error) {
    throw new Error('An error occurred. Please try again later.');
  }
};

export const postPreviewData = async (content) => {
  try {
    const res = await fetch("/api/preview", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(content)
    });
    const data = await res.json();
    return data.prediction;
  } catch (error) {
    throw new Error('An error occurred. Please try again later.');
  }
};
