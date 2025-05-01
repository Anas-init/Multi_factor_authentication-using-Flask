// Function to refresh the access token
async function refreshToken() {
    try {
        const response = await fetch('/refresh-token', {
            method: 'POST',
            credentials: 'include'
        });
        
        if (!response.ok) {
            throw new Error('Token refresh failed');
        }
        
        return true;
    } catch (error) {
        console.error('Token refresh failed:', error);
        window.location.href = '/login';
        return false;
    }
}

// Function to make authenticated API calls
async function makeAuthenticatedRequest(url, options = {}) {
    const defaultOptions = {
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json'
        }
    };
    
    const mergedOptions = {
        ...defaultOptions,
        ...options
    };
    
    try {
        let response = await fetch(url, mergedOptions);
        
        // If token is expired, try to refresh it
        if (response.status === 401) {
            const refreshSuccess = await refreshToken();
            if (refreshSuccess) {
                // Retry the original request with new token
                response = await fetch(url, mergedOptions);
            } else {
                throw new Error('Authentication failed');
            }
        }
        
        return response;
    } catch (error) {
        console.error('API request failed:', error);
        throw error;
    }
}

// Function to get current user info
async function getCurrentUser() {
    try {
        const response = await makeAuthenticatedRequest('/api/me');
        if (response.ok) {
            return await response.json();
        }
        throw new Error('Failed to get user info');
    } catch (error) {
        console.error('Failed to get current user:', error);
        return null;
    }
}

// Add event listener for token refresh
document.addEventListener('DOMContentLoaded', () => {
    // Refresh token every 5 minutes
    setInterval(refreshToken, 5 * 60 * 1000);
}); 