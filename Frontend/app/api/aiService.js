export const fetchGeneratedText = async (prompt) => {
    try {
      const apiUrl = `http://localhost:8000/generate_response?prompt=${encodeURIComponent(prompt)}`;
      console.log(apiUrl)
      
      const response = await fetch(apiUrl, {
        method: "GET", 
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
      });
      
      if (!response.ok) {
        throw new Error("Failed to fetch AI response. Status: ${response.status}");
      }
      
      // Return the fetched data 
      return await response.json(); 
    } catch (error) {
      console.error("API Error:", error);
      
      // Allow the component to handle the error
      throw error; 
    }
  };
  