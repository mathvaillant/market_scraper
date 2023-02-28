def cleanup_sring(raw_content: str, list: list) -> str:
  content = raw_content

  for entry in list:
    try:
      content = content.replace(entry, "")
    except:
      continue

  return content
