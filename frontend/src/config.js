// API Configuration for different environments
const getAPIBaseURL = () => {
  // In production on Railway, both frontend and backend are on same domain
  if (import.meta.env.PROD) {
    // Use same domain for Railway deployment (no CORS issues)
    return '';
  }
  // In development, use local backend
  return '';
};

export const API_BASE_URL = getAPIBaseURL();
export default API_BASE_URL;