const BACKEND_URL: string = "http://localhost:8000/api";
const CLOUDINARY_BASE_URL: string = "https://res.cloudinary.com/shayon-cloud/image/upload/v1691683509";
const MAX_SIGNIN_COOKIE_AGE: number = 60 * 60 * 24; // One day
const TOKEN_REFRESH_TIME: number = 1000 * 60 * 14; // in every 14 minutes


export {
    BACKEND_URL,
    CLOUDINARY_BASE_URL,
    MAX_SIGNIN_COOKIE_AGE,
    TOKEN_REFRESH_TIME
};