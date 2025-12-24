import api from "./api";

export const getDigitalTwin = (studentId) =>
  api.get(`/digital-twin/${studentId}`);
