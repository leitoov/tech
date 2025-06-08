import axios from "axios";
import { API_URL } from "../config";

export const registrarLog = async (mensaje, nivel = "INFO") => {
  try {
    await axios.post(`${API_URL}/logs`, { mensaje, nivel });
  } catch (error) {
    console.error("Error al registrar el log:", error);
  }
};