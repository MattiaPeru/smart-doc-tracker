export class UserFacingError extends Error {}

export function requestError(response, fallback) {
  if (response.status === 413) {
    return new UserFacingError("This file is too large. Choose a file smaller than 25 MB.");
  }
  if (response.status === 415) {
    return new UserFacingError("This file type is not supported. Choose a PDF or image.");
  }
  if (response.status >= 500) {
    return new UserFacingError("Something went wrong. Please try again in a moment.");
  }
  return new UserFacingError(fallback);
}

export function userMessage(error, fallback) {
  return error instanceof UserFacingError ? error.message : fallback;
}
