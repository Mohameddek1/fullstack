import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import api from "../api";
import { useState, useEffect } from "react";
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants";

function ProtectedRouter({ children }) {
    const [isAuthorized, setIsAuthorized] = useState(null);

    useEffect(() => {
        auth().catch(() => {
            setIsAuthorized(false);
        })
    })

    const refreshToken = async () => {
        // Function to refresh the access token
        const refreshToken = localStorage.getItem(REFRESH_TOKEN); // Retrieve the refresh token from local storage
        try {
            const res = await api.post("/api/token/refresh/", { refresh: refreshToken }); // Send a POST request to refresh the token endpoint
    
            if (res.status === 200) {
                // If the request is successful (status code 200), update the access token in local storage
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                setIsAuthorized(true); // Set authorization status to true
            } else {
                setIsAuthorized(false); // Set authorization status to false if the request fails
            }
        } catch (error) {
            console.log(error); // Log any errors to the console
            setIsAuthorized(false); // Set authorization status to false in case of an error
        }
    };
    

    const auth = async () => {
        // Function to authenticate the user
        const token = localStorage.getItem(ACCESS_TOKEN); // Retrieve the access token from local storage
        if (!token) {
            setIsAuthorized(false); // If no token exists, set authorization status to false
            return;
        }
        const decoded = jwtDecode(token); // Decode the JWT token to access its payload
        const tokenExpiration = decoded.exp; // Extract the expiration time from the token payload
        const now = Date.now() / 1000; // Get the current time in seconds
    
        if (tokenExpiration < now) {
            // If the token has expired, refresh it
            await refreshToken(); // Assuming you have a refreshToken function implemented
        } else {
            // If the token is still valid, set authorization status to true
            setIsAuthorized(true);
        }
    };
    

    if (isAuthorized === null) {
        return <div>Loading...</div>; // Render a loading indicator while authentication status is being determined
    }

    // Render the children if authorized, otherwise navigate to the login page
    return isAuthorized ? children : <Navigate to="/login" />;

    
}

export default ProtectedRouter;



















