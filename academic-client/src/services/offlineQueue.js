let offlineQueue = [];

export const addToQueue = (event) => {
  offlineQueue.push(event);
};

export const getQueue = () => offlineQueue;

export const clearQueue = () => {
  offlineQueue = [];
};
