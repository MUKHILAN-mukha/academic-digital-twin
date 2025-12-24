function EventPreview({ event }) {
  return (
    <div style={{ marginTop: 20 }}>
      <h3>Sent Academic Event</h3>
      <pre>{JSON.stringify(event, null, 2)}</pre>
    </div>
  );
}

export default EventPreview;
