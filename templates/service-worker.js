importScript('https://js.pusher.com/beams/service-worker.js');
<script src="https://js.pusher.com/beams/2.1.0/push-notifications-cdn.js"></script> script do SKD

 <script>
  const beamsClient = new PusherPushNotifications.Client({
    instanceId: 'ad961b7a-2772-4626-bf14-2cd23de153a7',
  });

  beamsClient.start()
    .then(() => beamsClient.addDeviceInterest('hello'))
    .then(() => console.log('Successfully registered and subscribed!'))
    .catch(console.error);
    
</script>   