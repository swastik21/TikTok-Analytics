def process_results(data):
  nested_values = ['video','author','music','stats','authorStats','challenges','duetInfo','textExtra','stickersOnItem']
  skip_values = ['challenges','duetInfo','textExtra','stickersOnItem']
  flattened_data = {}
  # Loop through each video
  for idx, value in enumerate(data):
    flattened_data[idx] = {}
    # Loop through each property in video
    for prop_idx, prop_value in value.items():
      # Check if nested
      if prop_idx in nested_values:
        if prop_idx not in skip_values:
          # Loop through each nested property
          for nested_idx, nested_value in prop_value.items():
            flattened_data[idx][prop_idx+'_'+nested_idx] = nested_value
      # If not nested, add it back to the flattened dictionary
      else:
        flattened_data[idx][prop_idx] = prop_value
  return flattened_data