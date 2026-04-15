const BASE_URL = "http://127.0.0.1:8000/api";

export const getAssets = async (role) => {
  const res = await fetch(`${BASE_URL}/assets/?role=${role}`);
  return res.json();
};