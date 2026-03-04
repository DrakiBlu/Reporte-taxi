import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.reportetaxi.app',
  appName: 'Reporte Taxi',
  webDir: 'www',
  server: {
    androidScheme: 'https'
  }
};

export default config;
