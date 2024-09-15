import axios from 'axios';

const apiService = {
  getApiStatus: async () => {
    try {
      const response = await axios.get('/api/status');
      return response.data;
    } catch (error) {
      console.error('Error fetching API status:', error);
      return [];
    }
  }
};

export default apiService;
