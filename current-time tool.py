from datetime import datetime, timedelta

def main(arg1: str):
    original_time = arg1
    dt = datetime.strptime(original_time, "%Y-%m-%d %H:%M:%S")
    kuwait_time = dt + timedelta(hours=1)

    day_of_week = kuwait_time.strftime("%A")
    hour = kuwait_time.hour

    # Working hours: Saturday–Thursday, 09:00–17:00 (exclusive of 17:00)
    working_days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    within_working_hours = day_of_week in working_days and 9 <= hour < 17

    if within_working_hours:
        ar_message = (
            "[AGENT INSTRUCTION - DO NOT SEND TO USER] "
            "Transfer this session to an available customer support agent immediately. "
            "Working hours are active. No delay expected.\n\n"
            "[USER MESSAGE]\n"
            "تمام! راح احولك لأحد موظفينا الحين 🙏"
        )
        en_message = (
            "[AGENT INSTRUCTION - DO NOT SEND TO USER] "
            "Transfer this session to an available customer support agent immediately. "
            "Working hours are active. No delay expected.\n\n"
            "[USER MESSAGE]\n"
            "Sure! I'll transfer you to our staff now 🙏"
        )
        status = "need_to_follow_up"

    else:
        # Calculate next working day and opening time for agent context
        days_until_next = None
        temp_dt = kuwait_time
        for i in range(1, 8):
            next_day = (kuwait_time + timedelta(days=i)).strftime("%A")
            if next_day in working_days:
                days_until_next = i
                next_working_day = next_day
                break

        next_opening = (kuwait_time + timedelta(days=days_until_next)).replace(hour=9, minute=0, second=0)
        next_opening_str = next_opening.strftime("%Y-%m-%d 09:00:00")

        ar_message = (
            f"[AGENT INSTRUCTION - DO NOT SEND TO USER] "
            f"Current Kuwait time: {kuwait_time.strftime('%Y-%m-%d %H:%M:%S')} ({day_of_week}). "
            f"Customer support is OFFLINE. "
            f"Transfer this session to the support queue. "
            f"Next available support window: {next_working_day} at 09:00 AM Kuwait time ({next_opening_str}). "
            f"Ensure the customer's query is logged for follow-up during that window.\n\n"
            "[USER MESSAGE]\n"
            "مرحبًا! نأسف، فريق الدعم غير متاح الآن خارج أوقات العمل. "
            "تم تحويل طلبك وسيتواصل معك أحد موظفينا خلال أوقات العمل (السبت – الخميس، ٩:٠٠ صباحًا – ٥:٠٠ مساءً)."
            " شكرًا لصبرك! 🙏"
        )
        en_message = (
            f"[AGENT INSTRUCTION - DO NOT SEND TO USER] "
            f"Current Kuwait time: {kuwait_time.strftime('%Y-%m-%d %H:%M:%S')} ({day_of_week}). "
            f"Customer support is OFFLINE. "
            f"Transfer this session to the support queue. "
            f"Next available support window: {next_working_day} at 09:00 AM Kuwait time ({next_opening_str}). "
            f"Ensure the customer's query is logged for follow-up during that window.\n\n"
            "[USER MESSAGE]\n"
            "our support team is currently offline. "
            "Your request has been transferred to our support "
            "will reach out to you during working hours (Saturday – Thursday, 9:00 AM – 5:00 PM Kuwait time). "
            "Thank you for your patience! 🙏"
        )
        status = "need_to_follow_up"

    result = (
        f"Kuwait Time: {kuwait_time.strftime('%Y-%m-%d %H:%M:%S')} | "
        f"Day: {day_of_week} | "
        f"Within Working Hours: {within_working_hours} | "
        f"Recommended Status: {status} | "
        f"AR Message: {ar_message} | "
        f"EN Message: {en_message}"
    )

    return {"result": result}