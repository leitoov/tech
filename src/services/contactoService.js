import axios from "axios";
import { API_URL } from "../config";

// Servicio para crear un contacto
export const crearContacto = async (contacto) => {
  try {
    const response = await axios.post(`${API_URL}/contacto`, contacto);
    // Registrar un log de éxito
    await registrarLog("Contacto creado exitosamente", "INFO");
    return response.data;
  } catch (error) {
    // Registrar un log de error
    await registrarLog(`Error al crear contacto: ${error.message}`, "ERROR");
    throw error.response ? error.response.data : "Error de conexión";
  }
};

// Servicio para registrar logs
export const registrarLog = async (mensaje, nivel = "INFO") => {
  try {
    await axios.post(`${API_URL}/logs`, { mensaje, nivel });
  } catch (error) {
    console.error("Error al registrar el log:", error);
  }
};