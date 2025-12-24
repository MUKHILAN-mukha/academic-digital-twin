const BASE_URL = "http://127.0.0.1:8000";

export async function fetchDigitalTwin(studentId) {
  const res = await fetch(`${BASE_URL}/digital-twin/${studentId}`);

  if (!res.ok) {
    throw new Error("Failed to fetch digital twin");
  }

  return res.json();
}
