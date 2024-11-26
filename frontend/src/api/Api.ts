export default class Api {
  private readonly baseUrl: string;
  constructor() {
    this.baseUrl = "http://localhost:8000";
  }

  async get(path: string) {
    const response = await fetch(`${this.baseUrl}${path}`);
    return await response.json();
  }

  async post(path: string, data?: any) {
    await fetch(`${this.baseUrl}${path}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
  }
}
