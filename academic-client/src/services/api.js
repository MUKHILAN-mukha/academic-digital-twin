import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 5000,
});

export const sendAcademicEvent = (event) => {
  return api.post("/academic-events", event);
};

export default api;
