# Use the official Node.js image to build the frontend
FROM node:18 as build-stage

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nodejs \
    npm             
# Install the dependencies
RUN npm install
RUN npm install @vue/cli -g
RUN npm install axios


# Copy the rest of the application code to the container
COPY . .

# Build the Vue.js project for production
RUN npm run build
CMD npm start
#CMD npm run serve

# Serve the build using a minimal server (nginx)
FROM nginx:alpine
# Copy the build files to nginx's default serving directory
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Run nginx server
CMD ["nginx", "-g", "daemon off;"]

