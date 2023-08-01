const BACKEND_URL: string = "http://localhost:8000/api";
const MAX_SIGNIN_COOKIE_AGE: number = 60 * 60 * 24; // One day
const TOKEN_REFRESH_TIME: number = 1000 * 60 * 9; // in every 9 minutes


export {
    BACKEND_URL,
    MAX_SIGNIN_COOKIE_AGE,
    TOKEN_REFRESH_TIME
};