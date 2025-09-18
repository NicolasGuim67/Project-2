from flask import Flask, request, jsonify
import pusher_push_notifications

print(pusher_push_notifications.__file__)

app = Flask(__name__)

# Corrigido o nome do parâmetro 'instance_id'
pn_client = pusher_push_notifications.PushNotifications(
    instance_id="ad961b7a-2772-4626-bf14-2cd23de153a7",
    secret_key="788A1209BB17744D295ECC5847921D378B704F2E1B53C0632CF37C8238098896",
)

# Rota corrigida: deve ser um caminho relativo, ex: /send-notification
@app.route("/send-notification", methods=["POST"])
def send_notifications():
    data = request.json
    user_id = data.get("user_id")
    message = data.get("message")

    if not user_id or not message:
        return jsonify({"status": "error", "message": "user_id e message são obrigatórios"}), 400

    try:
        # Para enviar a usuários específicos, use publish_to_users
        response = pn_client.publish_to_users(
            user_ids=[user_id],
            publish_body={
                "apns": {
                    "aps": {
                        "alert": message,
                    },
                },
                "fcm": {
                    "notification": {
                        "title": "Nova Notificação",
                        "body": message,
                    },
                },
            },
        )
        print("Notificação enviada:", response)
        return jsonify({"status": "success", "response": response}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
