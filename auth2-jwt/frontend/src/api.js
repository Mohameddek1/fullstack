import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

// Create an Axios instance with custom configurations
const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL // Sets the base URL for API requests using environment variables
});

// Add an interceptor to modify outgoing requests
api.interceptors.request.use(
    (config) => {
        // Retrieve the access token from local storage
        const token = localStorage.getItem(ACCESS_TOKEN);
        // If a token exists, add it to the request headers for authorization
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config; // Return the modified request configuration
    },
    (error) => {
        return Promise.reject(error); // Return a rejected promise for any request error
    }
);

export default api; // Export the configured Axios instance for use in other parts of the application
