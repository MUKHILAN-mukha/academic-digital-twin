import api from "./api";

export const createEvent = (data) =>
  api.post("/events/", data);
