import { ApolloServer } from "apollo-server";
import { ApolloGateway } from "@apollo/gateway";

const gateway = new ApolloGateway({
  serviceList: [
    {
      name: "product-service",
      url: "http://127.0.0.1:8000/graphql/",
    },
    {
      name: "shop-service",
      url: "http://127.0.0.1:8001/graphql/",
    },
  ],
  experimental_pollInterval: 10000,
});

const server = new ApolloServer({
  gateway,
  subscriptions: false,
});

server
  .listen({ port: 8002 })
  .then(({ url }) => {
    console.info(`🚀 Gateway available at ${url}`);
  })
  .catch((err) => console.error("❌ Unable to start gateway", err));
